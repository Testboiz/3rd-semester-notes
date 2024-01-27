## CSS

CSS adalah styling dari suatu HTML
CSS dapat diapply secara inline, `<style>` tag dan juga external .css file.

Syntax CSS Inline

````html
<div style="property:value">
	<p> Hello World </p>
</div>
````

Syntax CSS di `<style>` tag di `<head>` dan external CSS

````css
p {
	property1:value1;
	property2:value2;
	/*more stuff*/
	propertyN:valueN;
}
````

Cara melink css external

````html
	<link rel="stylesheet" href="/path/to/file.css">
	<!-- atau (umumnya untuk framework) -->
	<link rel="stylesheet" href="http://cdn.css-file-server.css">
````

### Selektor CSS

````html
<!DOCTYPE html>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style> 
	    /*tag selector*/
	    p {
		    color:red;
	    }
	    /*class selector*/
	    .class1 {
		    color:green;
	    }
	    /*alternatif class selector*/
	    p.class2 {
		    color:yellow;
	    }
	    /*ID selector*/
	    #id1 {
		    color:blue;
	    }
	    /*shorthand*/
	    .class3 {
		    padding : 1px,2px,3px,4px;
	    }
	    /*sama dengan
	    .class3 {
		    padding-top : 15px;
			padding-right : 20px;
			padding-bottom : 15px;
			padding-left : 20px;
	    }
	    */
	   /*Pseudo class => efek css ketika suatu hal terjadi*/
	   button:hover {
		   color:purple;
	   }
	    
    </style>
</head>
<body>
	<!-- CSS Pertama -->
	<p> Hello World </p>
	<!-- CSS Kedua -->
	<div class="class1">
	Hi World
	</div>
	<!-- CSS ketiga -->
	<p class:"class2"> Hellow world </p>
	<br>
	<!-- CSS Keempat -->
	<span id="id1"> hehe world </span>
</body>
</html>
````

## Unit CSS

Unit CSS ada yang bersifat absolut dan relatif:
Unit relatif :

* em => (berapa kali besarnya dari elemen yang ada)
* ex => (relatif dengan lebar font sekarang)
* ch => relatif dengan char "0"
* rem => relatif dengan root elemen font
* % => relatif terhadap container

Unit absolut :

* cm (10 mm)
* mm (control)
* in (25.4 mm)
* px ((px/ppi)/2.54 mm)
* pt ((pt/72) * 2.54 mm) (1/72 in and 1/12 pica)
* pc (pt/6) * 2.54 mm (1/6 in)

## Warna CSS

Ada berbagai cara untuk merepresentasikan warna di CSS

* Nama Inggrisnya
* Hexadecimal \#RRGGBB  dimana R G B adalah nilai diantara 0-f (hexadecimal)
* RGB => rgb(r,g,b) 0-255
* RGBA => rgba(r,g,b,a) dimana a = \[0-1\]

## Box Model

````
// An image is worth 1000 words
		|============================|
		|         PADDING            |
		|    |----BORDER---------|   |
		|    |     MARGIN        |   |
		|    |     [CONTENT]     |   |
		|    |     MARGIN        |   |
		|    |----BORDER---------|   |
		|         PADDING            |
		|============================|
		
````
