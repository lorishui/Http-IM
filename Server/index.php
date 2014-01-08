<?php
	require_once 'Common/LogicCenter.php';
	$info = $_REQUEST['info'];
	$logic = new LogicCenter();
	$logic->recvMsg($info);
	$logic->procMsg();

	