import java.util.*;

public class Deck {
	// want to migrate this to array list b/c removing from it and changing len
	Card[] cardDeck = new Card[52];

	public Deck() {
		this.cardDeck = cardDeck;
	}

	public void viewDeck() {
		for (Card card : cardDeck) {
			System.out.println(card.viewCard());
		}
	}

	public void generateDeck() {

		String[] suits = new String[] { "D", "H", "C", "S" };
		int count = 0;

		for (String suit : suits) {
			for (int rank = 2; rank < 15; rank++) {
				cardDeck[count] = new Card(suit, rank);
				count++;
			}
		}
	}

	public void shuffleDeck() {

		ArrayList<Card> cardDeckList = new ArrayList<Card>(Arrays.asList(cardDeck));

		Collections.shuffle(cardDeckList);

		Card[] cardDeck = cardDeckList.toArray(new Card[cardDeckList.size()]);

		this.cardDeck = cardDeck;
	}

	public Card dealCard() {
		// can use pop and remove at idx with arraylist
		return cardDeck[0];
	}

	public static void main(String[] args) {
		Deck john = new Deck();
		john.generateDeck();
		john.shuffleDeck();
		john.viewDeck();
	}
}