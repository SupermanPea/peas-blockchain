const peas = require('../../util/peas');

describe('peas', () => {
  it('converts number mojo to peas', () => {
    const result = peas.mojo_to_peas(1000000);

    expect(result).toBe(0.000001);
  });
  it('converts string mojo to peas', () => {
    const result = peas.mojo_to_peas('1000000');

    expect(result).toBe(0.000001);
  });
  it('converts number mojo to peas string', () => {
    const result = peas.mojo_to_peas_string(1000000);

    expect(result).toBe('0.000001');
  });
  it('converts string mojo to peas string', () => {
    const result = peas.mojo_to_peas_string('1000000');

    expect(result).toBe('0.000001');
  });
  it('converts number peas to mojo', () => {
    const result = peas.peas_to_mojo(0.000001);

    expect(result).toBe(1000000);
  });
  it('converts string peas to mojo', () => {
    const result = peas.peas_to_mojo('0.000001');

    expect(result).toBe(1000000);
  });
  it('converts number mojo to colouredcoin', () => {
    const result = peas.mojo_to_colouredcoin(1000000);

    expect(result).toBe(1000);
  });
  it('converts string mojo to colouredcoin', () => {
    const result = peas.mojo_to_colouredcoin('1000000');

    expect(result).toBe(1000);
  });
  it('converts number mojo to colouredcoin string', () => {
    const result = peas.mojo_to_colouredcoin_string(1000000);

    expect(result).toBe('1,000');
  });
  it('converts string mojo to colouredcoin string', () => {
    const result = peas.mojo_to_colouredcoin_string('1000000');

    expect(result).toBe('1,000');
  });
  it('converts number colouredcoin to mojo', () => {
    const result = peas.colouredcoin_to_mojo(1000);

    expect(result).toBe(1000000);
  });
  it('converts string colouredcoin to mojo', () => {
    const result = peas.colouredcoin_to_mojo('1000');

    expect(result).toBe(1000000);
  });
});
