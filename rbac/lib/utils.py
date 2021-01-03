from django.forms import model_to_dict
from django.http import JsonResponse


class BaseResponse(JsonResponse):
    def __init__(self,**kwargs):
        result={}
        for key in kwargs.keys():
            result[key] = kwargs[key]
        super().__init__(data=result)

def initMenu(menulist):
    key="parent"
    menuSet = set([menu for menuArr in menulist for menu in menuArr])
    menus = [model_to_dict(menu) for menu in menuSet]
    data2={}
    for item in menus:
        item["meta"] = {}
        item["meta"]["title"] = item["title"]
        item["meta"]["icon"]= item["icon"]
        del item["title"]
        del item["utm"]
        del item["ctm"]
        del item["icon"]
        if item[key]:
            if item[key] in data2:
                data2[item[key]]["children"].append(item)
            else:
                data2[item[key]] = {}
                data2[item[key]]["children"] = [item]
        else:
            if item["id"] not in data2:
                data2[item["id"]] = {}
            if "children" not in data2[item["id"]]:
                data2[item["id"]]["children"] = []
            data2[item["id"]]["meta"] = item['meta']
            data2[item["id"]]["path"] = item['path']
            data2[item["id"]]["redirect"] = item['redirect']
            data2[item["id"]]["component"] = item['component']
    menuNumber = sorted([x for x in data2.keys()])
    menuTree = [ data2[x] for x in  menuNumber]
    return menuTree