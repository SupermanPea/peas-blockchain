const weed = require('../../util/weed');

describe('weed', () => {
  it('converts number mojo to weed', () => {
    const result = weed.mojo_to_weed(1000000);

    expect(result).toBe(0.000001);
  });
  it('converts string mojo to weed', () => {
    const result = weed.mojo_to_weed('1000000');

    expect(result).toBe(0.000001);
  });
  it('converts number mojo to weed string', () => {
    const result = weed.mojo_to_weed_string(1000000);

    expect(result).toBe('0.000001');
  });
  it('converts string mojo to weed string', () => {
    const result = weed.mojo_to_weed_string('1000000');

    expect(result).toBe('0.000001');
  });
  it('converts number weed to mojo', () => {
    const result = weed.weed_to_mojo(0.000001);

    expect(result).toBe(1000000);
  });
  it('converts string weed to mojo', () => {
    const result = weed.weed_to_mojo('0.000001');

    expect(result).toBe(1000000);
  });
  it('converts number mojo to colouredcoin', () => {
    const result = weed.mojo_to_colouredcoin(1000000);

    expect(result).toBe(1000);
  });
  it('converts string mojo to colouredcoin', () => {
    const result = weed.mojo_to_colouredcoin('1000000');

    expect(result).toBe(1000);
  });
  it('converts number mojo to colouredcoin string', () => {
    const result = weed.mojo_to_colouredcoin_string(1000000);

    expect(result).toBe('1,000');
  });
  it('converts string mojo to colouredcoin string', () => {
    const result = weed.mojo_to_colouredcoin_string('1000000');

    expect(result).toBe('1,000');
  });
  it('converts number colouredcoin to mojo', () => {
    const result = weed.colouredcoin_to_mojo(1000);

    expect(result).toBe(1000000);
  });
  it('converts string colouredcoin to mojo', () => {
    const result = weed.colouredcoin_to_mojo('1000');

    expect(result).toBe(1000000);
  });
});
