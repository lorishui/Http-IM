<?php
	require_once 'NetMessage.php';
	//逻辑中心
	class LogicCenter
	{
		var $sendMsgList;
		var $recvMsgList;
		var $memcache;
		var $curSendMsg;
		
		function __construct()
		{
			$this->sendMsgList = array();
			$this->recvMsgList = array();
			$this->curSendMsg = new MsgList();
		}
		
		function addMsg($msg)
		{
			if($msg == NULL) return;
			if($this->curSendMsg == NULL)
			{
				$this->curSendMsg = new MsgList();
			}
			$this->curSendMsg->addMsg(json_encode($msg));
		}
		
		function sendMsg()
		{
			if($this->curSendMsg == NULL or $this->curSendMsg->msgnum <= 0) return;
			echo json_encode($this->curSendMsg);
			$this->curSendMsg->clear();
		}
		
		function recvMsg($recvInfo)
		{
			
			$info = json_decode($recvInfo);
			foreach ($info->msglist as $msg)
			{
				array_push($this->recvMsgList, $msg);
			}
		}
		
		function procMsg()
		{
			if(count($this->recvMsgList) <= 0) return;
			foreach($this->recvMsgList as $msg)
			{	
				$this->_procMsg($msg->opcode, $msg);
			}
			array_splice($this->recvMsgList,0);
		}
		
		function _procMsg($opcode,$msgObj)
		{
			switch($opcode)
			{
				case OpCode::OPC_CS_TEST:
					{
						$ret = new COPC_SC_TEST();
						$ret->name = "www";
						$this->addMsg($ret);
						$ret = new COPC_SC_TEST();
						$ret->name = "water";
						$this->addMsg($ret);
					}
					break;
			}
			
			$this->sendMsg();
		}
		
	}