
package taller11;
public class BitmaskSet {
	private int mask, size;

	public BitmaskSet() {
		this.size = 30;
		this.mask = 0;
	}

	public BitmaskSet(int size) {
		this.size = size;
		this.mask = 0;
	}

	public BitmaskSet(BitmaskSet o) {
		this.size = o.size();
		this.mask = o.mask();
	}

	public boolean isFull() {
		return mask == (1 << size) - 1;
	}

	public boolean contains(int k) {
		return (mask & (1 << k)) != 0;
	}

	public void add(int k) {
		mask |= 1 << k;
	}

	public int mask() {
		return mask;
	}

	public int size() {
		return size;
	}
}
