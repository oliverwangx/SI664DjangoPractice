import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

# Register your models here.
from unesco.models import Site, Category, States, Region, Iso

def run():
    fhand = open('unesco/whc.csv')
    reader = csv.reader(fhand)

    Site.objects.all().delete()
    Category.objects.all().delete()
    States.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    # Format
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python
    next(reader)
    for row in reader:
        print(row)
        try:
            y = int(row[3])
        except:
            y = None
        try:
            x = float(row[6])
        except:
            x = None
        c, created = Category.objects.get_or_create(name = row[7])
        s, created = States.objects.get_or_create(name = row[8])
        r, created = Region.objects.get_or_create(name = row[9])
        i, created = Iso.objects.get_or_create(name = row[10])
        a, created = Site.objects.get_or_create(name = row[0], year = y, category = c, description = row[1], justification  = row[2], longitude = float(row[4]), latitude = float(row[5]), area_hectares = x,states = s, region = r, iso = i )
        a.save()