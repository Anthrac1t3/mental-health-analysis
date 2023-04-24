<?php

// Establish database connection
$conn = pg_connect("host='127.0.0.1' port='5432' dbname='project' user='laxminarayanan.appusaravanan@my.utsa.edu' password='JZ2pzjFC&T^NGQcfvoU2'");

// Check if form is submitted
if(isset($_POST['submit'])){
    // Get search keyword from form input
    $search = $_POST['search'];

    // Query the database to search for matching records
    $query = "SELECT * FROM public.alone WHERE content LIKE '%$search%' ORDER BY tweet_id ASC LIMIT 100";
    $result = pg_query($conn, $query);

    // Display search results
    if(pg_num_rows($result) > 0){
        echo "<h2>Search Results</h2>";
        echo "<ul>";
        while($row = pg_fetch_assoc($result)){
            echo "<li>{$row['column1']} - {$row['column2']}</li>"; // Replace column1, column2 with your column names
        }
        echo "</ul>";
    } else {
        echo "No results found.";
    }

    // Close database connection
    pg_close($conn);
}
//phpinfo();
?>