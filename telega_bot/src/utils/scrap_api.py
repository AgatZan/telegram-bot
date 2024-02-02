from typing import Dict, List, Optional
import requests
from bs4 import BeautifulSoup


def scarap_api(
    url_page: str,
    tag_api_url: str,
    tag_api_name: Optional[str] = None,
    tag_api_annotation: Optional[str] = None,
    tag_api_auth: Optional[str] = None,
) -> Dict[str, Optional[List[str]]]:
    html = requests.get(url_page, timeout=10).text
    soup = BeautifulSoup(html, "html.parser")
    all_url = soup.select(tag_api_url)
    all_name = (
        [n.text for n in soup.find_all(tag_api_name)]
        if tag_api_name
        else [u.text for u in all_url]
    )
    all_annotation = (
        [a.text for a in soup.select(tag_api_annotation)]
        if tag_api_annotation
        else None
    )
    all_auth = [a.text for a in soup.select(tag_api_auth)] if tag_api_auth else None
    res = []
    for i, val in enumerate(all_url):
        res.append(
            {
                "name": all_name[i],
                "url": val.get("href"),
                "annotation": all_annotation and all_annotation[i],
                "auth": all_auth and all_auth[i],
            }
        )
    return res
