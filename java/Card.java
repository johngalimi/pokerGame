public class Card {
	String suit;
	int rank;

	public Card(String suit, int rank) {
		this.suit = suit;
		this.rank = rank;
	}

	public String viewCard() {
		String viewString = String.format("%s of %s", this.suit, this.rank);
		return viewString;
	}

	public static void main(String[] args) {
		Card john = new Card("D", 5);
		System.out.println(john.viewCard());
	}
}