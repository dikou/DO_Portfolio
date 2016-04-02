function check(e){
	if (e.email.value == e.emailconfirm.value){
		alert("Email confirmed! Thank you.");
		return true;
	}
	else{
		alert("Please correctly confirm your email.");
		return false;
	}
}

