# AppEndpointMap

A small static endpoint-map repository for Themadhood's Codes applications.

This repo is meant to be hosted with GitHub Pages and used as a stable public place where apps can fetch their current backend URLs without needing an app update.

## Purpose

Instead of hardcoding backend API URLs inside every app, each app downloads a small JSON map from this repo.

Example flow:

```text
App starts
↓
Load cached endpoint map
↓
If missing, expired, or backend fails, fetch fresh map from GitHub Pages
↓
Save map locally
↓
Use endpoint from the map
```

## GitHub Pages setup

1. Upload this repo to GitHub.
2. Go to the repo settings.
3. Open **Pages**.
4. Set source to the branch you want to publish.
5. Use the root folder `/`.
6. Save.

After GitHub Pages publishes, your maps should be available like this:

```text
https://YOUR-GITHUB-USERNAME.github.io/AppEndpointMap/maps/error.json
```

Or, if you use a custom domain later:

```text
https://your-domain.com/maps/error.json
```

## Recommended app behavior

Apps should not upload data to this repo. This repo only stores pointer files.

Recommended refresh rules:

```text
Fetch fresh map when:
- no local map exists
- local map is older than refresh_after_days
- the current endpoint fails
- the app version changed and requires updated paths
```

Recommended failure behavior:

```text
1. Try cached endpoint.
2. If it fails, fetch the newest map.
3. Retry once using the updated endpoint.
4. If that fails too, save the error locally for later upload.
```

## Main files

```text
index.html              Browser landing page
maps/error.json         Endpoint map for the Error system
maps/example.json       Example endpoint map template
schema.endpoint-map.md  Human-readable schema notes
LICENSE.txt            License for this endpoint-map repo
```

## Important note

GitHub Pages is good for static JSON files. It is not a backend server and should not be used for receiving POST uploads.
