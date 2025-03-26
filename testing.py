from astroquery.simbad import Simbad

result = Simbad.query_object("Betelgeuse")
print(result)
