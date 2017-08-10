import os
import logging
import requests
from urlparse import urljoin
from itertools import count
from dateutil.parser import parse
from pycountry import languages

from aleph.crawlers.crawler import DocumentCrawler

log = logging.getLogger(__name__)


class DocumentCloudCrawler(DocumentCrawler):
    DC_HOST = 'https://documentcloud.org/'
    DC_INSTANCE = 'documentcloud'
    DC_GROUP = None
    DC_QUERY = None

    def crawl_document(self, dc_document):
        foreign_id = '%s:%s' % (self.DC_INSTANCE, dc_document.get('id'))

        if self.skip_incremental(foreign_id):
            return

        document = self.create_document(foreign_id=foreign_id)
        document.source_url = dc_document.get('canonical_url')
        document.title = dc_document.get('title')
        document.author = dc_document.get('author')
        document.file_name = os.path.basename(dc_document.get('pdf_url'))
        document.mime_type = 'application/pdf'

        try:
            created = parse(dc_document.get('created_at'))
            document.add_date(created.date().isoformat())
        except:
            pass
        try:
            lang = languages.get(iso639_3_code=dc_document.get('language'))
            document.add_language(lang.iso639_1_code)
        except:
            pass

        self.emit_url(document, dc_document.get('pdf_url'))

    def crawl(self):
        search_url = urljoin(self.DC_HOST, 'search/documents.json')
        query = self.DC_QUERY or '*:*'
        if self.DC_GROUP:
            query = 'group:"%s"' % self.DC_GROUP
        for page in count(1):
            res = requests.get(search_url, params={
                'q': query,
                'per_page': 999,
                'page': page
            })
            data = res.json()
            documents = data.get('documents')
            if not len(documents):
                break
            for document in documents:
                self.crawl_document(document)


class SourceAfricaCrawler(DocumentCloudCrawler):
    DC_HOST = 'https://dc.sourceafrica.net/'
    DC_INSTANCE = 'sourceafrica'
    COLLECTION_ID = 'sourceafrica'
    COLLECTION_LABEL = 'sourceAFRICA'
    CRAWLER_NAME = 'sourceAFRICA'
