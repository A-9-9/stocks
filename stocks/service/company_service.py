from stocks.models import Company
from django.shortcuts import get_object_or_404

def createCompany(company_name: str) -> bool:
    company = Company(comp_name=company_name)
    company.save()
    return True
def retrieveCompanies():
    companies = Company.objects.all().order_by('id')
    return list(companies)

def retrieveCompanyByName(name: str) -> Company:
    company = get_object_or_404(Company, comp_name=name)
    return company
def retrieveComapnyById(id: str) -> Company:
    company = get_object_or_404(Company, pk=id)
    return company
def updateCompany(request: Company) -> Company:
    company = get_object_or_404(Company, pk=id)
    company = request
    company.save()
    return company
def deleteCompanyByName(name: str) -> bool:
    pass
def deleteCompanyById(id: str) -> bool:
    pass