from tendara_ai_challenge.Chroma.LLM import LLM
import chromadb
import uuid
from datetime import datetime
from tendara_ai_challenge.matching.search_profile import CompanySearchProfile
from tendara_ai_challenge.matching.models import Notice


class ChromaSingleton:
    _instance = None

    def __new__(cls, collection_name='notices'):
        """
        Ensure only one instance of ChromaSingleton is created
        and initialize Chroma client.
        """
        if not cls._instance:
            cls._llm = LLM()
            cls._instance = super(ChromaSingleton, cls).__new__(cls)
            cls._instance.client = chromadb.PersistentClient(path="db")
            cls._instance.collection_name = collection_name
            cls._instance.collection = cls._instance.client.get_or_create_collection(collection_name)
            if not cls._instance.collection:
                cls._instance.collection = cls._instance.client.create_collection(collection_name)

        return cls._instance

    def preprocess_metadata_value(self, notice: Notice) -> dict:
        """
        Preprocesses a metadata value for ChromaDB compatibility.
        :param notice: one notice instance to be processed
        :return : returns dict of metadata
        """
        metdata = {}
        for key, value in notice.dict().items():
            if key == 'search_text':
                continue
            if isinstance(value, datetime):
                metdata[key] = int(value.timestamp())
            elif isinstance(value, list):
                for index, item in enumerate(value):
                    metdata[f"{key}_{index}"] = item
            else:
                metdata[key] = value
        return metdata

    def add_batch_documents(self, documents):
        """
        Add a batch of documents (list of dictionaries) to the Chroma vector database.
        :param documents: List of dictionaries, each containing 'id' and 'text' (and other metadata)
        """
        # Prepare the batch of embeddings and metadata
        ids = []
        embeddings = []
        metadatas = []

        for doc in documents:
            doc_id = str(uuid.uuid4())  # Ensure each document has a unique ID
            metadata = self.preprocess_metadata_value(doc)
            embedding = self._llm.get_embedding(f"{doc.description} {doc.title}")
            ids.append(doc_id)
            embeddings.append(embedding)
            metadatas.append(metadata)

        # Add the batch of vectors to Chroma
        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            metadatas=metadatas,
            documents=[doc.json() for doc in documents]
        )

    def search(self, search_profile: CompanySearchProfile, top_k: int=3 ):
        """
        Search for the most similar vectors to the query in Chroma.
        :param search_profile: The search query text.
        :param top_k: Number of most similar results to return.
        :return: List of results with metadata.
        """
        query_embedding = self._llm.get_embedding(f"{search_profile.search_text}")
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            where=self.build_metadata_query(search_profile)
        )
        return [result for result in results['documents'][0] if result]

    def build_metadata_query(self, search_profile: CompanySearchProfile) -> dict:
        """
        Builds a metadata query for ChromaDB, ignoring None or empty parameters.
        :param search_profile: search profile to build the metadata based on it
        """
        metadata_query_list = []
        for key, value in search_profile.dict().items():
            if not value or key == "search_text":
                continue

            base_key = key.replace("max_", "").replace("min_", "")
            query_operator = None
            if key.startswith("max_"):
                query_operator = "$lte"
            elif key.startswith("min_"):
                query_operator = "$gte"

            if query_operator:
                metadata_query_list.append({base_key: {
                    query_operator: value.timestamp() if isinstance(value, datetime) else value}})
            elif isinstance(value, list):
                conditions = [{f"{key}_{i}": {"$in": value}} for i in range(len(value))]
                metadata_query_list.append(
                    {"$or": conditions} if len(conditions) > 1 else conditions[0])
            else:
                metadata_query_list.append({key: {"$eq": value}})

        if not metadata_query_list:
            return None
        return {"$and": metadata_query_list} if len(metadata_query_list) > 1 else \
        metadata_query_list[0]

