# PDF as a Service

Convert your `HTML` content into a `PDF` or `JPG` file.

## Running

### Docker

```bash
docker container run -d --rm -p 8080:80 diegoaceneves/pdf-aas
```

### On your machine

#### Requirements

This project was tested on `GNU/Linux Ubuntu 22.04 LTS`, with `python 3.10.6`

1. Clone this repository:

    ```bash
    git clone https://github.com/diegoaceneves/pdf-aas.git
    cd pdf-aas

    ```

2. Create a Virtual Environment and Install dependencies:

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

3. Running

    ```bash
    python app.py
    ```

## Endpoints

You can use this endpoints:

* /pdf
* /jpg

## Inputs

For both endpoints, we can use the same input file, this file can be to input a url or html.

### URL

```json
{"url":"https://google.com"}
```

### HTML

```json
{"html":"<html><body><h1>HTML Test</h1><p>Text test</p></body></html>"}
```

## How to use

### cUrl Example

```bash
# For PDF
curl -X POST \
  -H 'Content-type: application/json' \
  -d '{"url":"https://google.com"}' \
  --output file.pdf http://localhost:8080/pdf

#For JPG
curl -X POST \
  -H 'Content-type: application/json' \
  -d '{"html":"<html><body><h1>HTML Test</h1><p>Text test</p></body></html>"}' \
  --output file.jpg http://localhost:8080/jpg

```

### PHP Example

```php
<?php
    $HTML="
    <html>
     <body>
      <h1>HTML Test</h1>
      <p>Text test</p>
     </body>
    </html>";

    $ch = curl_init();
    $headers  = array ('Content-type: application/json');

    # For URL
    $postData = array ("url" => "https://google.com");

    # For HTML Code
    $postData = array ("html" => $HTML);

    # For PDF
    curl_setopt($ch, CURLOPT_URL,"http://localhost:8080/pdf");

    # For JPG
    curl_setopt($ch, CURLOPT_URL,"http://localhost:8080/jpg");

    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($postData));
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

    $pdf = curl_exec($ch);
    curl_close($ch);

    $outputPah = "/tmp/arquivo.pdf";
    $pdfFile = fopen($outputPah, 'w');
    fwrite($pdfFile, $pdf);
    fclose($pdfFile);
?>

```

## TO-DO

* Improve this `README` file.
* Change Docker image base to the clean alpine image
