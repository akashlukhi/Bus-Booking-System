<!DOCTYPE html>
<html>

<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">

	<title>Booking </title>

	<!-- Google font -->
	<link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet">

</head>

<body>
	<?php
		session_start();
		if(empty($_SESSION['username'])){
			header('Location: login.php');
			exit;
		}
	?>
	<link rel="stylesheet" type="text/css" href="css/ticketbookUI.css" />
	<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css" />
	<div id="booking" class="section">
		<div class="section-center">
			<div class="container">
				<div class="row">
					<div class="col-md-7 col-md-push-5">
						<div class="booking-cta">
							<h1>Make your reservation</h1>
							<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Animi facere, soluta magnam
								consectetur molestias itaque
								ad sint fugit architecto incidunt iste culpa perspiciatis possimus voluptates aliquid
								consequuntur cumque quasi.
								Perspiciatis.
							</p>
						</div>
					</div>
					<div class="col-md-4 col-md-pull-7">
						<div class="booking-form">
							<form  method = "post">
								<div class="form-group">
									<span class="form-label">Journy Date</span>
									<input class="form-control" type="date"name="date"  required >
								</div>
								<div class="row">
									<div class="col-sm-6">
										<div class="form-group">
											<span class="form-label">source</span>
											<input class="form-control" type="text" name="source" required>
										</div>
									</div>
									<div class="col-sm-6">
										<div class="form-group">
											<span class="form-label">destination</span>
											<input class="form-control" type="text" name="destination" required>
										</div>
									</div>
								</div>
								
								<div class="form-btn">
									<input type="submit" class="submit-btn" name="check" value="Check availability">
								</div>
								<?php
									$mysqli = new mysqli("localhost", "akash", "AKlukhi@123", "db");
									if(isset($_POST["check"])){
										$source = $_POST['source'];
										$destination = $_POST['destination'];
										$d = $_POST['date'];
										$_SESSION["source"] = $source;
										$_SESSION["destination"] = $destination;
										$_SESSION["d"] = $d;
										header('Location: showlist.php');
										exit;
									}
								?>
							</form>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</body>
</html>