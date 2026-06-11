"""
API Client for Backend Communication.
"""

import requests
from typing import Dict, List, Any
import logging

logger = logging.getLogger(__name__)

class APIClient:
    """
    API Client for communicating with the backend.
    """
    
    def __init__(self, base_url: str):
        """
        Initialize API Client.
        
        Args:
            base_url: Base URL of the backend API
        """
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
    
    def _request(self, method: str, endpoint: str, **kwargs) -> Dict:
        """
        Make an HTTP request.
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint
            **kwargs: Additional arguments for requests
        
        Returns:
            Response JSON
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {e}")
            return {}
    
    def get_scorecards(self) -> List[Dict]:
        """
        Get DQ scorecards.
        
        Returns:
            List of scorecard data
        """
        return self._request('GET', '/validation/scorecards')
    
    def get_quarantine_records(self, limit: int = 100) -> List[Dict]:
        """
        Get quarantined records.
        
        Args:
            limit: Maximum number of records to retrieve
        
        Returns:
            List of quarantined records
        """
        return self._request('GET', f'/quarantine/records?limit={limit}')
    
    def get_lineage_graph(self) -> Dict:
        """
        Get data lineage graph.
        
        Returns:
            Lineage graph data
        """
        return self._request('GET', '/lineage/graph')
    
    def get_alerts(self) -> List[Dict]:
        """
        Get active alerts.
        
        Returns:
            List of alerts
        """
        return self._request('GET', '/alerts/list')
    
    def get_health(self) -> Dict:
        """
        Get API health status.
        
        Returns:
            Health status
        """
        return self._request('GET', '/health')