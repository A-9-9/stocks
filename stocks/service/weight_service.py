from stocks.models import Weight, Company
from django.shortcuts import get_object_or_404
def createWeight(weight: Weight, requestCompany: Company) -> bool:
    company = get_object_or_404(Company, requestCompany.pk)
    company.weight_set.create(weight=weight)
    return True
def retrieveWeightByCompany(requestCompany: Company) -> Weight:
    # company = get_object_or_404(Company, requestCompany.pk)
    weight = requestCompany.weight_set.all().reverse()[0]
    return weight
def retrieveWeightsByCompanies(requestCompanies):
    li = []
    for i in requestCompanies:
        weight = retrieveWeightByCompany(i)
        li.append(weight)
    return li

def retrieveWeightByCompanyId(id: str) -> Weight:
    company = get_object_or_404(Company, id)
    weight = company.weight_set.all()
    return weight
def updateWeightByComapny(requestCompany: Company, weight: str) -> bool:
    requestCompany.weight_set.create(weight=weight)
    return True
def updateWeightByComapnyId(id: str, weight: str) -> bool:
    company = get_object_or_404(Company, id)
    company.weight_set.create(weight=weight)
    return True
def deleteWeightByComapny(company: Company) -> bool:
    pass
def deleteWeightByCompanyId(id: str) -> bool:
    pass