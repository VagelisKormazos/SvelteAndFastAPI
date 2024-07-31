<script>
    import Title from "$lib/title.svelte";
    import '../styles/global.css'
 </script>
 
 <header>
   <nav>
      <div class="siteName">
         Village <br> Raches
     </div>
      <div class="links">
         <a href="/">Home</a>
         <a href="/sailing">Sailing</a>
         <a href="/contact">Contact Us</a>
         <a href="/history">History</a>
         <a href="/stories">Our Stories</a>
      </div>
   </nav>
 </header>
 
 <main>
    <slot> </slot>

 </main>
 
 <footer>
    <p>Copyrihgt 2024 Vagelis Kormazos</p>
 </footer>
 
