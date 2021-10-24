if (window.location.href.indexOf('kiosk') > 0) {
    setTimeout(function () {
        try {
            const home_assistant_main =  document
                  .querySelector("body > home-assistant").shadowRoot
                  .querySelector("home-assistant-main");
            
            const drawer = home_assistant_main.shadowRoot
                  .querySelector("#drawer")
                  .style.display = 'none';
            
            home_assistant_main.style.setProperty("--app-drawer-width", 0);
            home_assistant_main.shadowRoot
                .querySelector("#drawer > ha-sidebar").shadowRoot
                .querySelector("div.menu > paper-icon-button")
                .style.display = 'none';
                
            var view1 = document.getElementById("root"); 
            view1.body.style.margin = '10px';
            
            window.dispatchEvent(new Event('resize'));
        }
        catch (e) {
            console.log(e);
        }
    }, 200);
}
