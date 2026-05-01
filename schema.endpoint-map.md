# Endpoint Map Schema

This is a simple human-readable schema for `.json` endpoint maps in this repo.

## Root fields

```json
{
	"map_name": "TMH_Error",
	"map_version": "1.0.0",
	"owner": "Themadhood's Codes",
	"last_updated": "2026-05-01",
	"refresh_after_days": 365,
	"notes": "Short note here.",
	"endpoints": {},
	"fallback": {}
}
```

## Endpoint fields

Each endpoint should use this shape:

```json
"error_upload": {
	"url": "https://example.com/api/error/upload",
	"method": "POST",
	"enabled": false,
	"description": "Main endpoint for uploading error records."
}
```

## Recommended app rules

```text
If enabled is false:
	Do not use that endpoint unless the app has a local override.

If the endpoint request fails:
	Fetch the newest endpoint map.
	Retry once using the updated endpoint.
	If retry fails, save the data locally.

If the cached map is older than refresh_after_days:
	Fetch the newest endpoint map before using it.
```
