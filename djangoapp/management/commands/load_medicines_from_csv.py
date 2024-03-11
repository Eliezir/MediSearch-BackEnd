import pandas as pd
from django.core.management.base import BaseCommand
from djangoapp.models import Medicine

class Command(BaseCommand):
    help = 'Load a medicines csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)
        


    def handle(self, *args, **options):
        def convert_to_boolean(value):
            if value == 'Sim':
                return True
            elif value == 'Não':
                return False
            else:
                return value
        
        field_mapping = {
            'CNPJ': 'cnpj',
            'SUBSTÂNCIA': 'substance',
            'LABORATÓRIO': 'laboratory',
            'PRODUTO': 'product',
            'APRESENTAÇÃO': 'presentation',
            'CLASSE TERAPEUTICA': 'therapeutic_class',
            'TIPO DE PRODUTO (STATUS DO PRODUTO)': 'product_type',
            'PF 12%': 'pf_12_percent',
            'PF 17%': 'pf_17_percent',
            'PF 18%': 'pf_18_percent',
            'PF 19%': 'pf_19_percent',
            'PF 19% ALC': 'pf_19_percent_alc',
            'PF 19,5% ALC': 'pf_19_5_percent_alc',
            'PF 20%': 'pf_20_percent',
            'PF 20% ALC': 'pf_20_percent_alc',
            'PF 20,5%': 'pf_20_5_percent',
            'PF 21%': 'pf_21_percent',
            'CAP': 'cap',
            'CONFAZ 87': 'confaz_87',
            'ICMS 0%': 'icms_0_percent',
            'RESTRIÇÃO HOSPITALAR': 'hospital_only',    
        }

        boolean_fields = ['cap', 'confaz_87', 'icms_0_percent', 'hospital_only']
        df = pd.read_csv(options['csv_file'])
        df = df.rename(columns=field_mapping)
        df = df.where(pd.notnull(df), None)

        df = df.filter(items=field_mapping.values())

        for field in boolean_fields:
            df[field] = df[field].apply(convert_to_boolean)

        for index, row in df.iterrows():
            Medicine.objects.create(**row.to_dict())