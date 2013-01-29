'''
Created on 07.11.2012

@author: steven
'''
import feedparser
from django.core.management.base import BaseCommand
from crime_main.models import Crime, District
import datetime
from dateutil import tz
from django.db.utils import IntegrityError
from django.db import transaction 

@transaction.commit_manually
class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print "Starting feed import ..."
        feed = feedparser.parse('http://www.berlin.de/polizei/presse-fahndung/_rss_presse.xml')
        for entry in feed.entries:
            title_parts = entry.title.split(' - ')
            if len(title_parts) > 1:
                title = title_parts[0]
                district_literal = title_parts[-1].strip()
                pub_date = datetime.datetime(*entry.published_parsed[:7], tzinfo=tz.gettz("Europe/Berlin"))
                crime = Crime.objects.get_or_create(full_text_link=entry.link)[0]
                crime.title = title
                crime.full_text_link = entry.link
                pub_date = datetime.datetime(*entry.published_parsed[:7], tzinfo=tz.gettz("Europe/Berlin"))
                try:
                    crime.save()
                except IntegrityError:
                    transaction.rollback()
                    continue
                try:
                    district = District.objects.get(name = district_literal)
                except District.DoesNotExist:
                    district = None
                if district is not None:
                    crime.districts.add(district)
                else:
                    
                    districts_literal = district_literal.split('/')
                    
                    for district_literal in districts_literal:
                        try:
                            district = District.objects.get(name = district_literal.strip())
                            crime.districts.add(district)
                        except District.DoesNotExist:
                            print u"'{}' not found...".format(district_literal)
                crime.save()
                transaction.commit()
                
