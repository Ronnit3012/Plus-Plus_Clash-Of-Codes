# Plus Plus

## Script for creating Virtual Environment using pyenv-win

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r ./server/requirements.txt
```

## Api endpoint

- /api/v1/analysis

### Request

```json
{
    imgURL: "string"
}
```

### Response

```json
{
    orignalImg: "string",
    annotatedImg: "string",
    isReal: boolean
    genderPreds: {
        male: float,
        female: float
    },
    gender: "string"
}
```
