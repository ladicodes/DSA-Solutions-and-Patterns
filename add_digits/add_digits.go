package add_digits

func AddDigits(n int) int {
	sum := 0
	// handle edge case
	if n == 0 {
		return 0
	}
	//positive integer
	if n > 0 {
		for n > 0 {
			sum += n % 10
			n = n / 10
		}
		return sum
	}
	//negative integer
	n = -n
	temp := n

	//Extract the first digit
	for n >= 10 {

		n = n / 10

	}
	firstDigit := n

	for temp > 0 {
		sum += temp % 10
		temp = temp / 10

	}

	return sum - (2 * firstDigit) //see .md file for explanation
}
