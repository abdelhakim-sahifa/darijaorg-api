# **Darija Words API**

This is a Flask-based API that provides access to a dataset of Darija (Moroccan language) words, including nouns, verbs, adjectives, adverbs, and pronouns. The data is stored in a Firebase Realtime Database, and the API allows users to retrieve, search, and filter words based on various criteria.

---

## **Features**

- Retrieve all words in the dataset.
- Filter words by type (e.g., noun, verb, adjective).
- Search for words by translation or word.
- Get detailed information about a specific word by its ID.

---

## **Setup Instructions**

### **Prerequisites**

1. **Python 3.x**: Ensure Python is installed on your system.
2. **Firebase Realtime Database**: The API connects to a Firebase Realtime Database. Make sure you have the database URL and the correct path to the data.

### **Installation**

1. Clone the repository:

   ```bash
   git clone https://github.com/darijaorg/darija-words-api.git
   cd darija-words-api
   ```

2. Install the required dependencies:

   ```bash
   pip install Flask requests
   ```

3. Set up environment variables (optional):

   - Create a `.env` file in the root directory and add the following:
     ```
     DATABASE_URL=https://darija2024-database-default-rtdb.firebaseio.com/
     PATH=darija-words.json
     ```

4. Run the Flask application:

   ```bash
   python app.py
   ```

   The API will start running at `http://127.0.0.1:5000`.

---

## **API Endpoints**

### **Base URL**

```
http://127.0.0.1:5000
```

### **1. Get All Words**

Retrieve all words in the dataset.

- **Endpoint**: `/words`
- **Method**: `GET`
- **Example Request**:
  ```
  GET http://127.0.0.1:5000/words
  ```
- **Example Response**:
  ```json
  {
    "data": {
      "a-noun-akhe-brother": {
        "type": "noun",
        "word": "akhe",
        "translation": "brother",
        "details": "-",
        "example": "-",
        "gender": "-",
        "phonetic": "-",
        "plural": "khout",
        "prounouns": {
          "her": "Khouha",
          "his": "Khouh",
          "my": "Khoya",
          "our": "Khouna",
          "their": "Khouhom",
          "your-pm": "Khoukom",
          "your-sf": "Khoueki",
          "your-sm": "Khouek"
        },
        "prounouns-plural": {
          "her": "khoutha",
          "his": "khouto",
          "my": "khouty",
          "our": "khoutna",
          "their": "khouthom",
          "your-pm": "khoutkom",
          "your-sf": "khouteki",
          "your-sm": "khoutek"
        },
        "singular": "-"
      },
      "a-noun-atay-tea": {
        "type": "noun",
        "word": "atay",
        "translation": "tea",
        "details": "-",
        "example": "Chrebt atay bezzaf = I drank a lot of tea",
        "gender": "masculine",
        "phonetic": "-",
        "plural": "uncountable",
        "prounouns": {
          "her": "-",
          "his": "-",
          "my": "-",
          "our": "-",
          "their": "-",
          "your-pm": "-",
          "your-sf": "-",
          "your-sm": "-"
        },
        "prounouns-plural": {
          "her": "-",
          "his": "-",
          "my": "-",
          "our": "-",
          "their": "-",
          "your-pm": "-",
          "your-sf": "-",
          "your-sm": "-"
        },
        "singular": "uncountable"
      }
    }
  }
  ```

---

### **2. Get Words by Type**

Retrieve words filtered by type (e.g., noun, verb, adjective).

- **Endpoint**: `/words/{type}`
- **Method**: `GET`
- **Example Request**:
  ```
  GET http://127.0.0.1:5000/words/noun
  ```
- **Example Response**:
  ```json
  {
    "data": {
      "a-noun-akhe-brother": {
        "type": "noun",
        "word": "akhe",
        "translation": "brother",
        "details": "-",
        "example": "-",
        "gender": "-",
        "phonetic": "-",
        "plural": "khout",
        "prounouns": {
          "her": "Khouha",
          "his": "Khouh",
          "my": "Khoya",
          "our": "Khouna",
          "their": "Khouhom",
          "your-pm": "Khoukom",
          "your-sf": "Khoueki",
          "your-sm": "Khouek"
        },
        "prounouns-plural": {
          "her": "khoutha",
          "his": "khouto",
          "my": "khouty",
          "our": "khoutna",
          "their": "khouthom",
          "your-pm": "khoutkom",
          "your-sf": "khouteki",
          "your-sm": "khoutek"
        },
        "singular": "-"
      }
    }
  }
  ```

---

### **3. Get Word by ID**

Retrieve details for a specific word by its ID.

- **Endpoint**: `/words/{word_id}`
- **Method**: `GET`
- **Example Request**:
  ```
  GET http://127.0.0.1:5000/words/a-noun-akhe-brother
  ```
- **Example Response**:
  ```json
  {
    "data": {
      "type": "noun",
      "word": "akhe",
      "translation": "brother",
      "details": "-",
      "example": "-",
      "gender": "-",
      "phonetic": "-",
      "plural": "khout",
      "prounouns": {
        "her": "Khouha",
        "his": "Khouh",
        "my": "Khoya",
        "our": "Khouna",
        "their": "Khouhom",
        "your-pm": "Khoukom",
        "your-sf": "Khoueki",
        "your-sm": "Khouek"
      },
      "prounouns-plural": {
        "her": "khoutha",
        "his": "khouto",
        "my": "khouty",
        "our": "khoutna",
        "their": "khouthom",
        "your-pm": "khoutkom",
        "your-sf": "khouteki",
        "your-sm": "khoutek"
      },
      "singular": "-"
    }
  }
  ```

---

### **4. Search Words**

Search for words by translation or word.

- **Endpoint**: `/search`
- **Method**: `GET`
- **Query Parameters**:
  - `q`: Search query (e.g., `brother`).
  - `type`: Filter by type (optional).
- **Example Request**:
  ```
  GET http://127.0.0.1:5000/search?q=brother
  ```
- **Example Response**:
  ```json
  {
    "data": {
      "a-noun-akhe-brother": {
        "type": "noun",
        "word": "akhe",
        "translation": "brother",
        "details": "-",
        "example": "-",
        "gender": "-",
        "phonetic": "-",
        "plural": "khout",
        "prounouns": {
          "her": "Khouha",
          "his": "Khouh",
          "my": "Khoya",
          "our": "Khouna",
          "their": "Khouhom",
          "your-pm": "Khoukom",
          "your-sf": "Khoueki",
          "your-sm": "Khouek"
        },
        "prounouns-plural": {
          "her": "khoutha",
          "his": "khouto",
          "my": "khouty",
          "our": "khoutna",
          "their": "khouthom",
          "your-pm": "khoutkom",
          "your-sf": "khouteki",
          "your-sm": "khoutek"
        },
        "singular": "-"
      }
    }
  }
  ```

---

## **Error Handling**

- **404 Not Found**: The requested resource does not exist.
  ```json
  {
    "error": "Resource not found"
  }
  ```
- **400 Bad Request**: Invalid query parameters or malformed request.
  ```json
  {
    "error": "Invalid request"
  }
  ```

---

## **Rate Limiting**

The API is rate-limited to 100 requests per hour per IP address. Exceeding this limit will result in a `429 Too Many Requests` response.

---

## **Deployment**

You can deploy this API using platforms like:

- **Heroku**
- **Google Cloud Run**
- **AWS Elastic Beanstalk**
- **PythonAnywhere**

Ensure the `DATABASE_URL` and `PATH` environment variables are set in your deployment environment.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Contact**

For questions or feedback, please contact:

- **Abdelhakim Sahifa**
- **Email**: abdelhakim.sahifa@gmail.com 
- **GitHub**: [abdelhakim-sahifa](https://github.com/abdelhakim-sahifa)
- - **Darijaorg.**
- **Email**: darija-org@gmail.com 
- **GitHub**: [Darijaorg](https://github.com/darijaorg)
