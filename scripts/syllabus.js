javascript: (() => {

    var allContent = [];

    const h1Elements = document.querySelectorAll('h1');

    var mainHeader = "";

    for (let element of h1Elements) {
        const h1_inner = element.innerHTML;
        if (h1_inner[0] !== "<") {
            mainHeader = h1_inner;
        }
    }

    allContent.push("# " + mainHeader);
    console.log("# " + mainHeader);
    console.log("");

    const url = location.href;
    allContent.push(url);
    console.log(url);
    console.log("");

    let all = document.getElementsByTagName("*");

    for (let element of all) {

        if (element.className == "_1g3eaodg") {
            const link = element.src;
            if (link.includes("https:")) {
                console.log("**" + element.alt + "**");
                allContent.push("![](" + link + ")");
                console.log("![](" + link + ")");
                console.log("");
            }
        }

        if (element.className == "m-t-1 description") {
            let originalString = element.innerHTML;
            let about = originalString.replace(/(<([^>]+)>)/gi, "");
            console.log("### About");
            allContent.push("### About");
            console.log(about);
            allContent.push(about);
            console.log("-------------");
            console.log("### Syllabus");
        }

        if (element.className == "headline-2-text bold m-b-2 ") {
            let originalString = element.innerHTML;
            let week = originalString.replace(/(<([^>]+)>)/gi, "");
            console.log("- " + week);
            allContent.push("- " + "**" + week + "**");
        }

        if (element.className == "_wmgtrl9 m-y-2") {
            let item = element.innerHTML;
            let removeSpan = item.replace(/<span[^>]*>([^<]*)<\/span>/, "");
            
            let itemStripped = removeSpan .replace(/(<([^>]+)>)/gi, "");

            console.log("  - " + itemStripped);
            allContent.push("  - " + itemStripped);
        }

    }



})();