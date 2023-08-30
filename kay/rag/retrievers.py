from kay.helpers.api import call_kay
from kay.helpers.exceptions import InvalidInput,ServerError


class KayRetriever:
    """
    Base class for retreiver
    """
    def _validate_dataset_id(self,dataset_id):
        available_dataset_id = ['company']
        if dataset_id not in available_dataset_id:
            raise InvalidInput(f'Invalid dataset_id : Has to be one of the following - {available_dataset_id}')
    
    def __init__(self, dataset_id="company", data_sources=None) -> None:
        """Init params."""
        self._validate_dataset_id(dataset_id)
        self.dataset_id = dataset_id
        self.data_sources = data_sources    
    
        
    def query(self,prompt,num_context=6,instruction=None) -> list:
        """Get contexts based on given prompt and post processing config"""
                
        dataset_config = {
            "dataset_id":self.dataset_id,
            "data_sources": self.data_sources
        }
        
        
        retrieval_config = {
            "num_context":num_context,
        }
        
        if instruction:
            retrieval_config['instruction'] = instruction
        
        embed_store_response = call_kay(prompt,dataset_config,retrieval_config)
        
        if embed_store_response.get('success') == "true":
            contexts = embed_store_response.get('contexts')
            return contexts
        else:
            raise ServerError(embed_store_response.get('error','Unknown Error'))