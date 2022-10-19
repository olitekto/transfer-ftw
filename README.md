# Transfer-FTW

<h2> Installations </h2>

<h3> Python</h3>
<p> Install dependencies using pip </p>
<p> pip install -r requirements.txt </p>
<p>Run in terminal : python3 ftwtransfer.py</p>
<h3> PHP</h3>
<p> Paste files in MAMP htdocs folder </p>
<p> Run using MAMP server </p>
<h3> Node JS </h3>
<p> Import in VScode  </p>
<p> Use npm to run: npm start </p>
<h3> JAVA Spring Boot </h3>
<p> Import in VS code </p>
<p> Run using Tomcat </p>

<h2> Usage </h2>
<p> JSON POST payload for all languages </p>
{
"account_bank": "044",
"account_number": "0690000044",
"amount": 500,
"narration": "New transfer",
"currency": "NGN",
"beneficiary_name": "Kwame Adew"
}
<h3> Python</h3>
<b> Initiate transfer </b>
<b> POST method </b>
<p> [LOCALHOST+URL]/initiateTransfer </p>
<b> Check status transder </b>
<b> GET method </b>
<p> http://127.0.0.1:80/checkTransfer?id=9898 </p>

<h3> Node JS </h3>
<b> Initiate transfer </b>
<b> POST method </b>
<p> http://localhost:3000/initiateTransfer </p>
<b> Check status transder </b>
<b> GET method </b>
<p> http://localhost:3000/checkStatus?id=9898 </p>

<h3> PHP </h3>
<b> Initiate transfer </b>
<b> POST method </b>
<p> http://localhost:8888/initiateTransfer </p>
<b> Check status transder </b>
<b> GET method </b>
<p> http://localhost:8888/checkStatus/4000 </p>

<h3> JAVA Spring Boot </h3>
<b> Initiate transfer </b>
<b> POST method </b>
<p> http://localhost:8080/initiateTransfer </p>
<b> Check status transder </b>
<b> GET method </b>
<p> http://localhost:8080/checkStatus?id=9898 </p>


