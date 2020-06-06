def CompoundInterest(Principal, Rate, Time, TimesInterestApplies):
    A = Principal * ((1 + (Rate/TimesInterestApplies)) ** (TimesInterestApplies*Time))
    return A
