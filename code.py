from geotiff import GeoTiff

tiff_file = open("A_soil.tif")
geo_tiff = GeoTiff(tiff_file, crs_code=3067)
print(geo_tiff)