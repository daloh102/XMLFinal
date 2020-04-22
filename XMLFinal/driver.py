from xml.dom import minidom
import xml.etree.ElementTree as ET
import lxml.html
from lxml import etree


def eingabe(data):
    doc = minidom.parse(data)
    return doc


def getWorkflowName(temp):
    rc = []
    for element in temp.getElementsByTagName("packagedElement"):
        new = element.getAttribute('name')
        rc.append(new)
    return rc


def getWorkflowId(temp):
    rc = []
    for element in temp.getElementsByTagName("packagedElement"):
        new = element.getAttribute('xmi:id')
        rc.append(new)
    return rc


def combineNameId(values, key):
    dictionary = dict(zip(values, key))
    return dictionary


def getWorkflowPathId(doc, workflowname):
    rc = []
    for element in doc.getElementsByTagName("edge"):
        if element.getAttribute('name') == workflowname:
            source = element.getAttribute('source')
            rc.append(source)
            target = element.getAttribute('target')
            rc.append(target)
    return rc


def getWorkflowPathName(dictionary, workflowlist):
    rc = []
    for element in workflowlist:
        # print(element)
        if element != dictionary.get(element):
            # print(element)
            rc.append(dictionary.get(element))
    return rc


def removeDuplicates(listname):
    s = []
    for element in listname:
        if (element != None) and (element not in s):
            s.append(element)
    return s


def convertListToXML(listname):
    usrconfig = ET.Element("workflow")
    usrconfig = ET.SubElement(usrconfig, "worflow")
    for user in range(len(listname)):
        usr = ET.SubElement(usrconfig, "Schritt")
        usr.text = str(listname[user])
    tree = ET.ElementTree(usrconfig)
    tree.write("test.xml", encoding="utf-8", xml_declaration=True)


def getWorkflowEdge(document):
    rc = []
    for element in document.getElementsByTagName("edge"):
        new = element.getAttribute('name')
        rc.append(new)
    return rc


data = input("Dateiname: ")
var = eingabe(data)
workflowname = getWorkflowEdge(var)
newworkflowname = removeDuplicates(workflowname)

for element in newworkflowname:
    new = getWorkflowName(var)
    newer = getWorkflowId(var)
    dictionary = combineNameId(newer, new)
    newtest = getWorkflowPathId(var, element)
    newesttest = getWorkflowPathName(dictionary, newtest)
    removed = removeDuplicates(newesttest)

    convertListToXML(removed)
    xslt_doc = etree.parse("driverstylesheet.xslt")
    xslt_transformer = etree.XSLT(xslt_doc)
    source_doc = etree.parse("test.xml")
    output_doc = xslt_transformer(source_doc)
    output_doc.write(element+".html", pretty_print=True)
    print(element+".html")
    print("Hello Test")
