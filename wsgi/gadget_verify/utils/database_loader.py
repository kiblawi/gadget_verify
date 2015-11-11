import os, sys, django

parentabs = os.path.abspath("..")
sys.path.insert(0,parentabs)

os.environ.setdefault("DJANGO_SETTINGS_MODULE","gadget_verify.settings")
django.setup()
from verify.models import Gene, Abstract, Query

datafile = 'query_data.txt'

with open(datafile,'rU') as file:
    for line in file:
        splitline = line.split('\t')
        true_relevant_string = splitline[0]
        true_relevant = False
        if true_relevant_string in ['TRUE','True','T']:
            true_relevant = True
        entrez = int(splitline[1])
        symbol = splitline[2].replace('"','')
        gene_name = splitline[3].replace('"','')
        synonyms = splitline[4].replace('"','')
        abstract_name = splitline[5].replace('"','')
        author = splitline[6].replace('"','')
        pmlink = splitline[7]
        pmid = int(splitline[8])
        queryname = splitline[9].strip()
        
        q = Query(name=queryname)
        q.save()
        
        if Gene.objects.filter(entrez=entrez,query=queryname).exists():
            g = Gene.objects.get(entrez=entrez,query=queryname)
        else:
            g = Gene(name=gene_name,query=q,entrez=entrez,symbol=symbol,true_relevance=true_relevant,synonyms=synonyms)
            g.save()

        a = Abstract(pmid=pmid,title=abstract_name,author=author,link=pmlink)
        a.save()
        g.abstracts.add(a)



