<?php

// Establish database connection
$conn = pg_connect("host='10.28.28.13' port='5432' dbname='project' user='project' password='c%QQrKWfhowU5!AC94X'");

// Check if form is submitted
if(isset($_POST['submit'])){
    // Get search keyword from form input
    $search = $_POST['search'];

    // Query the database to search for matching records
    $query = "select * from (SELECT * FROM public.alone
union all
select * from public.blissful
union all
select * from public.bored
union all
select * from public.depressed
			   union all
select * from public.food
			   union all
select * from public.happy
			   union all
select * from public.joyful
			   union all
select * from public.loneliness
			   union all
select * from public.outing
			   union all
select * from public.sad
			   union all
select * from public.stressed
			   union all
select * from public.travel
			   union all
select * from public.vacation
			  ) mt
			  where content like '%$search%'
ORDER BY tweet_id ASC, author ASC LIMIT 100";
    $result = pg_query($conn, $query);
    
   // Display the navbar
    echo '<link href="./assets/css/styles.css" rel="stylesheet">';
    echo '<body class="bg-primary">';
    echo '<nav class="navbar navbar-expand-lg navbar-dark bg-secondary">';
    echo '<div class="container">';
    echo '<a class="navbar-brand" href="index.html">LSDM Project</a>';
    echo '<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>';
    echo '<div class="collapse navbar-collapse" id="navbarSupportedContent">';
    echo '<ul class="navbar-nav ms-auto mb-2 mb-lg-0">';
    echo '<li class="nav-item"><a class="nav-link active" aria-current="page" href="index.html">Home</a></li>';
    echo '<li class="nav-item"><a class="nav-link" href="education.html">Insights</a></li>';
    echo '<li class="nav-item"><a class="nav-link" href="work.html">Results</a></li>';
    echo '<li class="nav-item"><a class="nav-link" href="about me.html">Project Description</a></li>';
    echo '<li class="nav-item"><a class="nav-link" href="contact.html">Team Info</a></li>';
    echo '</ul>';
    echo '</div>';
    echo '</div>';
    echo '</nav>';
    // Display search results
    //if(pg_num_rows($result) > 0){
   //     echo "<h2>Search Results</h2>";
   //     echo "<ul>";
    //    while($row = pg_fetch_assoc($result)){
    //        echo "<li>{$row['author']} - {$row['content']} - {$row['mood']}</li>";
     //   }
   //     echo "</ul>";
   // } else {
    //    echo "No results found.";
   // }
    
 /*   echo "<link href="./assets/css/styles.css" rel="stylesheet">";
      echo "<body class="bg-primary">";
        echo "<!-- Responsive navbar-->";
        echo "<nav class="navbar navbar-expand-lg navbar-dark bg-secondary">";
            echo "<div class="container">";
                echo "<a class="navbar-brand" href="index.html">LSDM Project</a>";
              echo "<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>";
                echo "<div class="collapse navbar-collapse" id="navbarSupportedContent">";
                    echo "<ul class="navbar-nav ms-auto mb-2 mb-lg-0">";
                        echo "<li class="nav-item"><a class="nav-link active" aria-current="page" href="index.html">Home</a></li>";
                        echo "<li class="nav-item"><a class="nav-link" href="education.html">Insights</a></li>";
						echo "<li class="nav-item"><a class="nav-link" href="work.html">Results</a></li>";
						echo "<li class="nav-item"><a class="nav-link" href="about me.html">Project Description</a></li>";
						echo "<li class="nav-item"><a class="nav-link" href="contact.html">Team Info</a></li>";
                                            echo "</ul>";

                echo "</div>";

            echo "</div>";

        echo "</nav>";  */

    
    // Display search results in a table
   
       if(pg_num_rows($result) > 0){
        echo '<h2>Search Results</h2>';
        echo '<table style="border: 1px solid black">';
        echo '<tr>';
        echo '<th style="border: 1px solid black; padding: 5px">Author</th>'; // Replace with your column names
        echo '<th style="border: 1px solid black; padding: 5px">Content</th>';
        echo '<th style="border: 1px solid black; padding: 5px">Mood</th>'; // Replace with your column names
        echo '</tr>';
        while($row = pg_fetch_assoc($result)){
            echo '<tr>';
            echo '<td style="border: 1px solid black; padding: 5px">'.$row['author'].'</td>'; // Replace column1 with your column name
            echo '<td style="border: 1px solid black; padding: 5px">'.$row['content'].'</td>'; // Replace column2 with your column name
            echo '<td style="border: 1px solid black; padding: 5px">'.$row['mood'].'</td>';
            echo '</tr>';
    }
    }

    // Close database connection
    pg_close($conn);
}
//phpinfo();
?>
