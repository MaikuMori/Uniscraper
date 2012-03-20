#Uniscraper

Just a simple crawler to scrape some data for University course.

Requires *Python 2.7*.

##Usage

Go to the base directory and execute command:

    scrapy crawl FuelStationSpider

That will (re)generate _FuelStationSpider___results.xml_ file.

You can also run 

    scrapy crawl http://www.1188.lv/katalogs/K%C4%81zu%20saloni%20

or any other category url to crawl that specific category.

##XML Schema

The file _UniscraperPlaces.xsd_ contains XML Schema for the output.

##Example output

    <?xml version="1.0" encoding="utf-8"?>
    <Places xmlns="UniscraperPlaces">
      <Place>
        <Name>"Rietumu nafta" SIA</Name>
        <Branche>Degvielas uzpildes stacijas</Branche>
        <Address>Ganību iela 31, Kuldīga, Kuldīgas nov., LV-3301</Address>
        <Lat>56.9586351</Lat>
        <Lon>21.9902223</Lon>
        <Email>rietumi@gmail.com</Email>
        <Phone>63322684</Phone>
        <Keywords>
          <value>Degviela.</value>
          <value>Marķētās degvielas.</value>
          <value>Degvielas un citu naftas produktu tirdzniecība</value>
          <value>vairumtirdzniecība.</value>
          <value>Diennakts DUS.</value>
          <value>Motoru eļļas.</value>
          <value>Smērvielas.</value>
          <value>Eļļa auto eļļas.</value>
          <value>Degvielas piegāde.</value>
          <value>Lauksaimnieku degviela.</value>
          <value>Bezakcīzes degviela</value>
        </Keywords>
      </Place>
    </Places>
    
The actual output isn't pretty printed as it's supposed to be read by a program and not a person.
If that's really needed, make a bug.

##Dependencys

* Scrapy >= 0.14