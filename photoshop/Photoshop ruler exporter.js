// https://superuser.com/a/793711

function getGuides(doc) {
    var i, l;
    var g, d;
    var guides = [[],[]];

    for (i=0,l=doc.guides.length; i<l; i++) {
        g = doc.guides[i];
        d = (g.direction === Direction.HORIZONTAL) ? 0 : 1;
        guides[d].push(parseFloat(g.coordinate)+0);
    }
    return guides;
}

function listGuides(doc) {
    var report = "Guides in " + doc.name;

    var guides = getGuides(doc);
    var directions = ["Horizontal", "Vertical"];
    var units = (doc.guides.length) ?  doc.guides[0].coordinate.toString().split(" ")[1] : "px";

    var i, j, l;
    var d;

    for (d=0; d<2; d++) {
        report += "\n\n" + directions[d] + ":\n";
        if (guides[d].length) {
            guides[d].sort(function(a,b){return a-b;});
            for (i=0,l=guides[d].length; i<l; i++) {
                report += "\n" + (i+1) + ") " + guides[d][i] + " " + units;
            }
        } else {
            report += "\nNone";
        }
    }
    return report;
}


//Dispatch
if (BridgeTalk.appName === "photoshop") {
    alert(listGuides(app.activeDocument));
}