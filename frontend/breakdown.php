<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Orders</title>
  </head>
  <body>
    <h1> Order Breakdown </h1>
    <p><strong>Enter names separated by commas below.</strong></p>
    <?php 
      # fetch array for items => prices from dict_helper.py
      $result = json_decode(exec('python dict_helper.py'), true);
    ?>
    <div class = "search-form">
        <?php 
          # iteratively create forms for each item in the receipt
          echo "<form action=\"\" method=\"POST\"><br>";
          $i = 0;
          foreach ($result as $key => $value) {
            echo "Who ordered " . $key . "? <br>";
            echo "<input type=\"text\" name=\"names" . $i . "\"><br><br>";
            $i++;
          }
          echo "<input type=\"submit\" value=\"Submit\" class=\"submit-search\">";
          echo "</form><br>";
          
          # create php array
          $names_list = array();
          $j = 0;
         
          # for each $i...
          foreach ($result as $key => $value) {
            $post_string = "names{$j}";
            $name_list[$j] = $_POST[$post_string];
            $j++;
          }

          # array of names: $name_list (contains string of names for each field, separated by commas)
          # process this array in python

        ?>
    </div>
  </body>
</html>