let items = [
    {
        btn: document.getElementById("who_typed"),
        modal: document.getElementById("modal2"),
        close: document.getElementById("close2"),
        save: document.getElementById("save2"),
        cancel: document.getElementById("cancel2")
    }, {
        btn: document.getElementById("why_typed"),
        modal: document.getElementById("modal1"),
        close: document.getElementById("close1"),
        save: document.getElementById("save1"),
        cancel: document.getElementById("cancel1")
    },
    {
        btn: document.getElementById("what_typed1"),
        modal: document.getElementById("modal3"),
        close: document.getElementById("close3"),
        save: document.getElementById("save3"),
        cancel: document.getElementById("cancel3")
    },
    {
        btn: document.getElementById("what_typed2"),
        modal: document.getElementById("modal4"),
        close: document.getElementById("close4"),
        save: document.getElementById("save4"),
        cancel: document.getElementById("cancel4")
    }
]

items.map((item, index) => {
    item.btn.addEventListener("click", (e) => {
        e.preventDefault();
        item.modal.style.display = "unset";
        // add overflow-hidden when users open the modal
        $('body').css("overflow", "hidden");
    })

    item.close.addEventListener("click", (e) => {
        e.preventDefault();
        item.modal.style.display = "none";
        // add overflow-auto when users close the modal
        $('body').css("overflow", "auto");
    })

    item.cancel.addEventListener("click", (e) => {
        e.preventDefault();
        item.modal.style.display = "none";
        // add overflow-auto when users close the modal
        $('body').css("overflow", "auto");
    })
})

var menu, menuItems, panelSnapInstance;


document.addEventListener("DOMContentLoaded", function () {
    menu = document.querySelector('.menu');
    menuItems = menu.querySelectorAll('.menu-button');

    panelSnapInstance = new PanelSnap();
    panelSnapInstance.on('activatePanel', activateMenuItem);

    menuItems.forEach(function (menuItem) {
        menuItem.addEventListener('click', onButtonClick);
    });

    // 
    document.querySelectorAll("a").forEach(link => {
        link.target = "_blank";
    })

    // set session id on page load


    function uniqueId() {
        // desired length of Id
        var idStrLen = 32;
        // always start with a letter -- base 36 makes for a nice shortcut
        var idStr = (Math.floor((Math.random() * 25)) + 10).toString(8) + "_";
        // add a timestamp in milliseconds (base 36 again) as the base
        idStr += (new Date()).getTime().toString(8) + "_";
        // similar to above, complete the Id using random, alphanumeric characters
        do {
            idStr += (Math.floor((Math.random() * 35))).toString(8);
        } while (idStr.length < idStrLen);

        return (idStr);
    }   
    
    // generate new session id if it doesn't exist
    if (!sessionStorage.getItem('session')) {
        sessionStorage.setItem("session", uniqueId());
        // console.log("Session id:", sessionStorage.getItem('session'));
    }

});

function activateMenuItem(panel) {
    menuItems.forEach(function (menuItem) {
        menuItem.classList.remove('active');
    });

    var panelName = panel.getAttribute('data-panel')
    var menuItem = menu.querySelector('button[data-panel="' + panelName + '"]');
    menuItem.classList.add('active');
    updateContent(panelName);
}

function onButtonClick(e) {
    var panelName = e.target.getAttribute('data-panel')
    var panel = document.querySelector('section[data-panel="' + panelName + '"]');
    panelSnapInstance.snapToPanel(panel);
}

async function updateContent(elem) {
    // first delete all typed text
    deleteAll();
    if (document.getElementById("why_desc").classList.contains("active"))
        document.getElementById("why_desc").classList.remove("active");
    if (document.getElementById("who_desc").classList.contains("active"))
        document.getElementById("who_desc").classList.remove("active");
    if (document.getElementById("what_desc").classList.contains("active"))
        document.getElementById("what_desc").classList.remove("active");

    switch (elem) {
        case 'second':
            document.getElementById("who_desc").classList.add("active");
            setTimeout(async () => {
                await typeSentence("Are you one of us?", '#who_typed');
            }, 1200);
            break;
        case 'third':
            document.getElementById("why_desc").classList.add("active");
            setTimeout(async () => {
                await typeSentence("How did you get here?", '#why_typed');
            }, 1200);
            break;
        case 'fourth':
            document.getElementById("what_desc").classList.add("active");
            setTimeout(async () => {
                await typeSentence("What do you do?", '#what_typed1');
                await typeSentence("How can we work together?", '#what_typed2');
            }, 1200);
            break;
        default:
            break;
    }
}

// -------------- typing animations --------------------
async function typeSentence(sentence, eleRef, delay = 40) {
    const letters = sentence.split("");
    let i = 0;
    while (i < letters.length) {
        await waitForMs(delay);
        $(eleRef).append(letters[i]);
        i++
    }
    return;
}

function deleteSentence(eleRef) {
    const sentence = $(eleRef).html();
    const letters = sentence.split("");
    let i = 0;
    while (letters.length > 0) {
        letters.pop();
        $(eleRef).html(letters.join(""));
    }
}

function deleteAll() {
    deleteSentence("#who_typed");
    deleteSentence("#why_typed");
    deleteSentence("#what_typed1");
    deleteSentence("#what_typed2");
}

function waitForMs(ms) {
    return new Promise(resolve => setTimeout(resolve, ms))
}


// get all user responses
function getResponses() {
    let responses = localStorage.getItem("responses");
    return responses;
}

// save reponse

