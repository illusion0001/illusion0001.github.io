const categories = { patches: [{ url: `/patches/2023/01/02/t2-bow-charge-sway-bugfix/`, date: `02 Jan 2023`, title: `Bug Fix: The Last of Us Part 2 Broken Aim After Using The Bow`},{ url: `/patches/2022/06/12/Gravite2-FrameratePatch-Update/`, date: `12 Jun 2022`, title: `Gravity Rush 2 (Gravity Daze 2) Unofficial 60FPS Patch Now Playable on PS4/PS4 Pro`},{ url: `/patches/2022/05/10/Motorstorm-Framerate-Patch/`, date: `10 May 2022`, title: `Patches and Improvements for MotorStorm Titles (RPCS3)`},{ url: `/patches/2022/05/01/GOW-PS3-FPS-Patches/`, date: `01 May 2022`, title: `Framerate Patch and Intro Skip for God Of War 3/Ascension (RPCS3)`},{ url: `/patches/2022/04/18/Fromsoftware-Framepacing/`, date: `18 Apr 2022`, title: `Framepacing Fixes for Fromsoftware Titles (PS4)`},{ url: `/patches/2022/03/09/Big3-MPBeta-Lan/`, date: `09 Mar 2022`, title: `Uncharted 3 Multiplayer Beta Now Playable Without PSN (PS3)`},{ url: `/patches/2022/02/05/uncharted-tlou-introskips/`, date: `05 Feb 2022`, title: `Intro Skip Patches for Uncharted and The Last of Us`},{ url: `/patches/2021/12/19/Gravite2-FrameratePatch/`, date: `19 Dec 2021`, title: `Initial Framerate Patch Release (Work-In-Progress) for Gravity Rush 2`},{ url: `/patches/2021/12/04/t1-nailbomb-softlock-patch/`, date: `04 Dec 2021`, title: `University Nailbomb Softlock Fix for The Last of Us (PS3, PS4)`},{ url: `/patches/2021/10/20/RatchetPS3-FPSUnlock/`, date: `20 Oct 2021`, title: `Framerate Unlock Patches for Ratchet and Clank PS3 titles (RPCS3)`},{ url: `/patches/2021/10/14/MC4-FPSPatch/`, date: `14 Oct 2021`, title: `Dynamic FPS Patch for Midnight Club: Los Angeles`},{ url: `/patches/2021/10/02/Overbite-FPSFixes/`, date: `02 Oct 2021`, title: `Patches for MediEvil (PS4 Remake)`},{ url: `/patches/2021/09/09/AlienIsolation-Patches/`, date: `09 Sep 2021`, title: `Patches and Enhancements for Alien: Isolation (PS4)`},{ url: `/patches/2021/07/16/GOW-MLAA-RPCS3-Patch/`, date: `16 Jul 2021`, title: `Graphics Patches for God of War 3 and Ascension for RPCS3`},{ url: `/patches/2021/07/07/W3Witcher-ResPatch/`, date: `07 Jul 2021`, title: `The Witcher 3 60FPS and Grahpics Settings Research for PS4`},{ url: `/patches/2021/07/01/QDR.Infraworld-Res-Letterbox-Patch/`, date: `01 Jul 2021`, title: `Patches for Beyond Two Souls 60FPS, Blackbars Remover and More`},{ url: `/patches/2021/06/27/oodle-res-framerate-patches/`, date: `27 Jun 2021`, title: `Patches for The Order 1886 60FPS, 16:9 Aspect Ratio and More`},{ url: `/patches/2021/06/25/t1-ps3-mlaa-fix/`, date: `25 Jun 2021`, title: `Non MLAA Bug Fixes for The Last of Us (RPCS3)`},{ url: `/patches/2021/03/20/t2-silencer-cheat/`, date: `20 Mar 2021`, title: `Porting and Improving Cheat Codes in The Last of Us`},{ url: `/patches/2021/02/18/uc2-quit-menu-bug-fix/`, date: `18 Feb 2021`, title: `Fixing A Rare Bug in Uncharted 2 (PlayStation 3/4)`},{ url: `/patches/2021/02/16/t1r-head-crash-bug-fix/`, date: `16 Feb 2021`, title: `Solving the Infected's Severed Head Crash Bug in The Last of Us (PlayStation 4)`},{ url: `/patches/2021/02/15/t1-head-crash-bug-fix/`, date: `15 Feb 2021`, title: `Solving the Infected's Severed Head Crash Bug in The Last of Us (PlayStation 3)`},{ url: `/patches/2021/02/11/ms3-mlaa/`, date: `11 Feb 2021`, title: `Removing Morphological Anti-Aliasing from MotorStorm: Apocalypse`},{ url: `/patches/2021/02/10/t1r-improve-loading/`, date: `10 Feb 2021`, title: `Improved Loading for The Last of Us Remastered`},], }

console.log(categories);

window.onload = function () {
  document.querySelectorAll(".article-category").forEach((category) => {
    category.addEventListener("click", function (e) {
      const posts = categories[e.target.innerText.replace(" ","_")];
      console.log(posts);
      let html = ``
      posts.forEach(post=>{
        html += `
        <a class="modal-article" href="${post.url}">
          <h4>${post.title}</h4>
          <small class="modal-article-date">${post.date}</small>
        </a>
        `
      })
      document.querySelector("#category-modal-title").innerText = e.target.innerText;
      document.querySelector("#category-modal-content").innerHTML = html;
      document.querySelector("#category-modal-bg").classList.toggle("open");
      document.querySelector("#category-modal").classList.toggle("open");
    });
  });

  document.querySelector("#category-modal-bg").addEventListener("click", function(){
    document.querySelector("#category-modal-title").innerText = "";
    document.querySelector("#category-modal-content").innerHTML = "";
    document.querySelector("#category-modal-bg").classList.toggle("open");
    document.querySelector("#category-modal").classList.toggle("open");
  })
};