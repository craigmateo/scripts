javascript: (() => {

    var allContent = [];

    const h2Elements = document.querySelectorAll('h2');

    var mainHeader = "";

    for (let element of h2Elements) {
        const h2_inner = element.innerHTML;
        if (h2_inner[0] !== "<") {
            mainHeader = h2_inner;
        }
    }

    allContent.push(mainHeader);

    const all = document.getElementsByTagName("*");

    for (let element of all) {

        if (element.className == "rc-FormPartsQuestion__numberCell") {
            let originalString = element.innerHTML;
            let strippedString = originalString.replace(/(<([^>]+)>)/gi, "");
            let num = strippedString.substring(0, strippedString.indexOf('.') + 1);
            allContent.push("");
            allContent.push(num + "NUMBER");
        }

        if (element.tagName.toLowerCase() === 'input') {
            if (element.checked) {
                allContent.push("- [x]");
            } else {
                allContent.push("- [ ]");
            }
        }

        if (element.tagName.toLowerCase() === 'img') {
            const link = element.src;
            if (link.includes("https:")) {
                allContent.push("![](" + link + ")");
            }
        }

        if (element.className == "cmlToHtml-content-container") {
            let originalString = element.innerHTML;
            let strippedString = originalString.replace(/(<([^>]+)>)/gi, "");
            allContent.push(strippedString);
        }

    }

    var cleaned = [];
    cleaned.splice(1);

    var firstPass = [];

    for (let element of allContent) {
        if (element !== "NUMBER") {
            firstPass.push(element);
        }
    }

    for (let i = 0; i < firstPass.length; i++) {

        let element = firstPass[i];

        if (i == "0") {
            cleaned.push("# " + element);
        } else if (element.includes("NUMBER")) {
            var question = element.replace('NUMBER', '') + " " + firstPass[i + 1];
            cleaned.push(question);
            i++;
            continue;
        } else if (element.includes("- [ ]") || element.includes("- [x]")) {
            var option = element + " " + firstPass[i + 1];
            cleaned.push(option);
            i++;
            continue;
        } else {
            cleaned.push(element);
        }

    }

    for (let element of cleaned) {

        console.log(element);

    }

})();