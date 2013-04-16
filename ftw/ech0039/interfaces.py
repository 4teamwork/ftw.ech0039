from zope.interface import Interface


class IECH0039Exportable(Interface):
    """Marker interface for all eCH-0039 exportable content.
    """

    def add_to(marshaller):
        """Defines how to add the exportable to a marshaller.

        * If self is a document or dossier according to ECH0039 call
          `add_document` or `add_dossier` on the marshaller.
        * If neither self nor its children should appear in the export file
          `pass`.
        * If only selfs children should appar in the export file call `add` on
          the marshaller.

        """

#    def uuid(self):
#        """Return the exportable's uuid.
#        """
#
#    def title(self):
#        """Return the exportable's title.
#        """
#
#    def workflow_state(self):
#        """Return the exportable's workflow state.
#        """


class IECH0039Dossier(IECH0039Exportable):
    """Marker interface for eCH-0039 dossiers.
    """

    def get_children():
        """Return the children of this dossier.

        A dossier can contain other dossiers or documents.
        """


class IECH0039Document(IECH0039Exportable):
    """Marker interface for eCH-0039 documents.
    """
