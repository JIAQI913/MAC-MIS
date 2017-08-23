from django_tables2 import tables

from myapps.models import Project, Job


class ProjectTable(tables.Table):
    class Meta:
        model = Project
        attrs = {'class': 'table table-striped'}

class JobTable(tables.Table):
    class Meta:
        model = Job
        fields = ('Job_ID','Job_company','Job_position','Job_address','Stu_ID')
        labels = {'Stu_ID': u'hhhhh'}
        attrs = {'class': 'table table-striped'}