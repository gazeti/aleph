
DOC_TYPE = 'document'

DOC_MAPPING = {
    "_id": {
        "path": "id"
    },
    "_all": {
        "enabled": True
    },
    "dynamic": "strict",
    "properties": {
        "id": {"type": "string", "index": "not_analyzed"},
        "title": {"type": "string", "index": "analyzed"},
        "slug": {"type": "string", "index": "not_analyzed"},
        "collection": {"type": "string", "index": "not_analyzed"},
        "archive_url": {"type": "string", "index": "not_analyzed"},
        "source_url": {"type": "string", "index": "not_analyzed"},
        "name": {"type": "string", "index": "analyzed"},
        "extension": {"type": "string", "index": "analyzed"},
        "mime_type": {"type": "string", "index": "analyzed"},
        "text": {"type": "string", "index": "analyzed"},
        "summary": {"type": "string", "index": "analyzed"},
        "normalized": {"type": "string", "index": "analyzed"},
        "created_at": {"type": "date", "index": "not_analyzed"},
        "updated_at": {"type": "date", "index": "not_analyzed"},
        "entities": {
            "_id": {
                "path": "id"
            },
            "type": "nested",
            "include_in_parent": True,
            "properties": {
                "id": {"type": "string", "index": "not_analyzed"},
                "citation": {"type": "string", "index": "analyzed"},
                "score": {"type": "integer", "index": "not_analyzed"},
                "url": {"type": "string", "index": "not_analyzed"},
                "source": {"type": "string", "index": "not_analyzed"},
                "source_url": {"type": "string", "index": "not_analyzed"}
            }
        }
    }
}