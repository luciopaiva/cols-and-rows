
- unify all scripts into exie.py
- make a variation of `cols` that doesn't require matching the entire line; for instance, given the following input:

      m_VisualOffset="20.0000000000" m_Desc="Some desc" m_FlattenWidth="9.0000000000" m_roadId="0"

  I want to be able to run:

      exie other-cols 'm_FlattenWidth="(.*?)"' '\1'

  And get only this as the output:

      9.0000000000

  Notice that I didn't have to match the whole line, as I would've done with cols:

      exie cols '^.*?m_FlattenWidth="(.*?)".*$' '\1'

- for lists of fields (instead of TSV and CSV files) in which the field name appears before every value, we could do
  something like this:

      exie pick m_FlattenWidth

  And get:

      "9.0000000000"

  As the output. We could go even further and pick lists of fields with their respective types:

      exie pick m_FlattenWidth as number, m_Desc as string

  And get:

      9 "Some desc"
