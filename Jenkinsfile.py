pipeline{
	agent any
	stages{
		stage("Cleaning Stage"){
			steps{
				echo "this is cleaning stage"
				}
		stage("Testing Stage"){
			steps{
				echo "this is testing stage"
				}
		}
	}