# Ex.05 Design a Website for Server Side Processing
## Date: 03.04.2024

## AIM:
To design a website to find surface area of a Right Cylinder in server side.

## FORMULA:
Surface Area = 2Πrh + 2Πr<sup>2</sup>
<br>r --> Radius of Right Cylinder
<br>h --> Height of Right Cylinder

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
<!DOCTYPE html>
<html>
<head>
    <title>Surface Area of Right Cylinder</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 0;
        }

        .container {
            width: 400px;
            margin: 50px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        h2 {
            text-align: center;
            margin-bottom: 20px;
            color: #333;
        }

        form {
            margin-bottom: 20px;
        }

        label {
            display: block;
            margin-bottom: 5px;
            color: #555;
        }

        input[type="text"] {
            width: calc(100% - 22px);
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 3px;
        }

        input[type="submit"] {
            width: 100%;
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 3px;
            cursor: pointer;
        }

        input[type="submit"]:hover {
            background-color: #45a049;
        }

        .result {
            background-color: #f9f9f9;
            padding: 15px;
            border-radius: 3px;
        }

        .result label {
            font-weight: bold;
            color: #555;
        }

        .result input[type="text"] {
            width: calc(100% - 22px);
            padding: 10px;
            margin-top: 5px;
            border: 1px solid #ccc;
            border-radius: 3px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Surface Area of Right Cylinder</h2>
        <form method="POST">
            {% csrf_token %}
            <label for="radius">Enter the Radius:</label>
            <input type="text" id="radius" name="radius" value="{{ r }}">
            <label for="height">Enter the Height:</label>
            <input type="text" id="height" name="height" value="{{ h }}">
            <input type="submit" value="Calculate">
        </form>
        <div class="result">
            <label for="surfacearea">Surface Area:</label>
            <input type="text" id="surfacearea" name="surfacearea" value="{{ surfacearea }}" readonly>
        </div>
    </div>
</body>
</html>

```


## SERVER SIDE PROCESSING:
![alt text](<Screenshot 2024-04-03 211746.png>)

## HOMEPAGE:
![alt text](<Screenshot 2024-04-03 125712.png>)

## RESULT:
The program for performing server side processing is completed successfully.
