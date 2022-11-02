import { jsPDF } from "jspdf";
import autoTable from 'jspdf-autotable';
import my_json from "./input1.json" assert { type: 'json' };

// change According to INPUT
let outputCheckPoints = ["testCaseId", "respDesc", "respCode", "respCode1", "respCode2", "respDesc1"]
let dbCheckPoints = ['respDesc2', 'isSaltedPassword']
let summaryCheckPoints = ['prviousRecords', "currentRecords", "testCasesNotExecuted", "testCasesExecuted", "additionalRecords", "additionalRecords1", "additionalRecords2"]

const getHeadings = (checkPoint, format = 4, isTestCaseId = true) => {
    const lowerCaseHeadings = checkPoint.map(item => item.toLowerCase())
    let oneHeadList = []
    let allHeadList = []
    let testCaseId = ""
    let count = -1
    if (lowerCaseHeadings.includes("testcaseid") && isTestCaseId) {
        let index = lowerCaseHeadings.indexOf("testcaseid")
        checkPoint.splice(index, 1)
        testCaseId = "testCaseId"
        oneHeadList.push(testCaseId)
        isTestCaseId = true
        count = 0
    }
    else if(isTestCaseId) {
        testCaseId = "testCaseId"
        oneHeadList.push(testCaseId)
        count = 0
    }

    for (let i = 0; i < checkPoint.length; i++) {
        if (count == format) {
            allHeadList.push(oneHeadList)
            if (isTestCaseId) {
                oneHeadList = [testCaseId]
                count = 0
            }
            else {
                oneHeadList = []
                count = -1
            }
        }
        oneHeadList.push(checkPoint[i]);
        count++
    }
    if (oneHeadList.length) {
        allHeadList.push(oneHeadList)
    }
    return allHeadList
}

const emptyInit = (checkPoint, len) => {
    var value = 'N/A'; // by default
    let checkPointLen = checkPoint.length
    let myFullGrid = []
    for (let i = 0; i < checkPointLen; i++) {
        var myGrid = [...Array(len)].map(e => Array(checkPoint[i].length).fill(value));
        myFullGrid.push(myGrid)
    }
    return myFullGrid
}


const populateValue = (headings, body, my_json) => {
    for (let i = 0; i < headings.length; i++) {
        for (let j = 0; j < my_json.length; j++) {
            for (let z = 0; z < headings[i].length; z++) {
                let value = my_json[j][headings[i][z]]
                if (value) {
                    body[i][j][z] = value
                }
            }
        }
    }
    return body
}

const generatePDFReport = (summaryCheckPoints, outputCheckPoints, dbCheckPoints, my_json) => {

    let myJsonLength = my_json.length - 1

    const allOutputHeadings = getHeadings(outputCheckPoints); 
    const alldbheadings = getHeadings(dbCheckPoints); 
    const allSummaryHeadings = getHeadings(summaryCheckPoints, 4, false); 

    let emptyOutputBody = emptyInit(allOutputHeadings, myJsonLength)
    let emptydbBody = emptyInit(alldbheadings, myJsonLength)
    let emptySummaryBody = emptyInit(allSummaryHeadings, 1)
    const jsonSummaryBody = [my_json.pop()]

    const outputBody = populateValue (allOutputHeadings, emptyOutputBody, my_json) 
    const dbBody = populateValue (alldbheadings, emptydbBody, my_json) 
    const summaryBody = populateValue (allSummaryHeadings, emptySummaryBody, jsonSummaryBody) 

    // Generate PDF
    const doc = new jsPDF();   

    doc.text(15, 10, 'Summary :');
    let column_width = [{
        0: { cellWidth: 30 },
        1: { cellWidth: 30 },
        2: { cellWidth: 45 },
        3: { cellWidth: 40 },
        4: { cellWidth: 40 },
    }]
    for (let i = 0; i < allSummaryHeadings.length; i++) {
        doc.autoTable({
            columnStyles: column_width[i],
            startY:  typeof doc.autoTable.previous.finalY === 'undefined' ? 20 : doc.autoTable.previous.finalY + 10,
            theme: 'grid',
            head: [allSummaryHeadings[i]],
            body: summaryBody[i],
        })
    };

    doc.text(15,  doc.autoTable.previous.finalY + 10, 'Test Cases Info: ');
    doc.text(15,  doc.autoTable.previous.finalY + 20, '==>Output Checkpoints: ');

    doc.autoTable.previous.finalY += 20
    
    for (let i = 0; i < allOutputHeadings.length; i++) {
        doc.autoTable({
            startY:  doc.autoTable.previous.finalY + 10,
            theme: 'grid',
            head: [allOutputHeadings[i]],
            body: outputBody[i],
        })
    };

    doc.text(15, doc.autoTable.previous.finalY + 10, '==>DB Check Points: ');
    doc.autoTable.previous.finalY += 10
    for (let i = 0; i < alldbheadings.length; i++) {
        doc.autoTable({
            startY:  doc.autoTable.previous.finalY + 10,
            theme: 'grid',
            head: [alldbheadings[i]],
            body: dbBody[i],
        })
    };

    doc.save('table.pdf')
}
// main function
generatePDFReport(summaryCheckPoints, outputCheckPoints, dbCheckPoints, my_json)