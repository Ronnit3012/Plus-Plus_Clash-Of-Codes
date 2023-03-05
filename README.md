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
  "imgURL": "string"
}
```

### Response

```json
{
    originalImg: "string",
    annotatedImg: "string",
    isReal: boolean,
    isRealPreds: {
        real: float,
        fake: float
    },
    genderPreds: {
        male: float,
        female: float
    },
    gender: "string",
    age: int,
    agePreds: [{}],
    faceProb: "string",
    message: "string"
}
```
