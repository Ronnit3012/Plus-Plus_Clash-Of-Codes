# Plus Plus

## Demo
- Video: https://youtu.be/PyK2xdq7cBs
- Presentation: [Canva](https://www.canva.com/design/DAFcTQBnZvc/bpLNfaWS9yVd2W5dieasMg/edit?utm_content=DAFcTQBnZvc&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

## Script for creating Virtual Environment using pyenv-win

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r ./server/requirements.txt
```
## Challenges faced
- Low Testing Accuracy of ML Model: Split distorted faces, animes, avatar, cartoon characters into multiple classes instead of single class - "fake faces".
- Small size of dataset: Performed augmentation of images to increase dataset size and better train the ML Model.

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

## Contributors
- [Devang Shah](https://github.com/Devang-Shah-49/)
- [Krish Panchal](https://github.com/beastkp)
- [Ronnit Mirgh](https://github.com/Ronnit3012)
- [Sairaaj Surve](https://github.com/SairaajSurve)
